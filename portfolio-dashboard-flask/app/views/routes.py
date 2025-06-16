from flask import Blueprint, jsonify, request, send_file
import pandas as pd
import io

from app.controllers.main_controller import get_all_data
from app.models.data_model import fetch_asset_data

views = Blueprint('views', __name__)

@views.route('/api/data', methods=['GET'])
def get_data():
    try:
        btc = float(request.args.get('btc', 0.5))
        usd = float(request.args.get('usd', 0.5))
        total = btc + usd

        # Normalize weights if they don’t sum to 1
        if total != 1.0:
            btc /= total
            usd /= total

        weights = [btc, usd]
        data = get_all_data(weights)
        return jsonify(data)

    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input for weights"}), 400


# additional code for formatting to CSV etc.
import io
from flask import send_file

@views.route('/api/export', methods=['GET'])
def export_csv():
    try:
        btc = float(request.args.get('btc', 0.5))
        usd = float(request.args.get('usd', 0.5))
        total = btc + usd
        btc /= total
        usd /= total
        weights = [btc, usd]

        # Get raw price and return data
        df = fetch_asset_data()
        returns = df.pct_change().dropna()

        # Combine and flatten for export
        combined = pd.concat([df, returns.add_suffix('_returns')], axis=1).dropna()

        # Save to buffer
        buffer = io.StringIO()
        combined.to_csv(buffer)
        buffer.seek(0)

        return send_file(
            io.BytesIO(buffer.getvalue().encode()),
            mimetype='text/csv',
            as_attachment=True,
            download_name='portfolio_data.csv'
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500
