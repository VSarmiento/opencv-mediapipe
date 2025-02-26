from mediapipe.model_maker import gesture_recognizer

data = gesture_recognizer.DataLoader.from_folder('gesture_model/reduced_data')

train_set, eval_set = data.split(0.8)
model = gesture_recognizer.create(
    train_set,
    model_spec='gesture_recognizer.task',
    epochs=10,
    batch_size=32
)

loss, accuracy = model.evaluate(eval_set)
print(f"Accuracy: {accuracy:.2f}")
model.export(export_dir='exported_model')