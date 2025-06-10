loss, acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {acc:.2%}")
