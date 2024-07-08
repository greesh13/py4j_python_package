#!/bin/bash

# Set the correct path to the py4j jar
PY4J_PATH="$(dirname $0)/py4j-0.10.9.5.jar"

# Compile the Java file
javac -cp $PY4J_PATH -d $(dirname $0) $(dirname $0)/MathOperations.java

# Run the Java Gateway file
java -cp "$PY4J_PATH:$(dirname $0)" mypackage.MathOperations > $(dirname $0)/gateway.log 2>&1 &
