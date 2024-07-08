
Commands to run:

python -m venv venv
source venv/bin/activate
pip install py4j
pip show py4j
python test_math_operations.py


Steps to run the package on target system:

unzip py4j.zip
cd py4j
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
chmod +x mypackage/run_java_gateway.sh
./mypackage/run_java_gateway.sh
python test_math_operations.py