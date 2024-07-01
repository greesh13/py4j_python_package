import os
import time
from py4j.java_gateway import JavaGateway, GatewayParameters

def start_java_gateway():
    # Check if the server is already running
    try:
        gateway = JavaGateway(gateway_parameters=GatewayParameters(auto_convert=True))
        # Test if the connection works
        gateway.entry_point.add(1, 1)
    except Exception:
        # If not running, start the server
        script_path = os.path.join(os.path.dirname(__file__), 'run_java_gateway.sh')
        os.system(script_path)
        time.sleep(2)  # Give some time for the server to start
        gateway = JavaGateway(gateway_parameters=GatewayParameters(auto_convert=True))
    return gateway

class MathOperations:
    def __init__(self):
        self.gateway = start_java_gateway()
        self.entry_point = self.gateway.entry_point

    def add(self, a, b):
        return self.entry_point.add(a, b)

    def subtract(self, a, b):
        return self.entry_point.subtract(a, b)
