from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Wild Rydes'
    }), 200

@app.route('/api/rides')
def get_rides():
    """Get available rides"""
    rides = [
        {
            'id': 1,
            'destination': 'Downtown',
            'fare': 15.00,
            'driver': 'John Doe'
        },
        {
            'id': 2,
            'destination': 'Airport',
            'fare': 25.00,
            'driver': 'Jane Smith'
        },
        {
            'id': 3,
            'destination': 'Beach',
            'fare': 20.00,
            'driver': 'Mike Johnson'
        }
    ]
    return jsonify(rides), 200

@app.route('/api/rides/<int:ride_id>')
def get_ride(ride_id):
    """Get specific ride details"""
    rides = {
        1: {'id': 1, 'destination': 'Downtown', 'fare': 15.00, 'driver': 'John Doe', 'distance': '5 miles'},
        2: {'id': 2, 'destination': 'Airport', 'fare': 25.00, 'driver': 'Jane Smith', 'distance': '12 miles'},
        3: {'id': 3, 'destination': 'Beach', 'fare': 20.00, 'driver': 'Mike Johnson', 'distance': '8 miles'}
    }
    ride = rides.get(ride_id)
    if ride:
        return jsonify(ride), 200
    return jsonify({'error': 'Ride not found'}), 404

@app.route('/api/status')
def status():
    """Service status endpoint"""
    return jsonify({
        'status': 'operational',
        'service': 'Wild Rydes API',
        'version': '1.0.0',
        'environment': os.getenv('ENVIRONMENT', 'production')
    }), 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)
