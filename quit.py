<script>
    window.addEventListener("beforeunload", function () {
        navigator.sendBeacon("/shutdown");
    });
</script>


@app.route('/shutdown', methods=['POST'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    os._exit(0)  # Terminate the entire application
    return "Server shutting down..."
