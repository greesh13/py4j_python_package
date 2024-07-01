#!/bin/bash
java -cp $(dirname $0)/../py4j0.10.9.5.jar:$(dirname $0)/MathOperations.jar MathOperations > $(dirname $0)/gateway.log 2>&1 &
