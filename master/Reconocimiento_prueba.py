from imageai.Prediction.Custom import CustomImagePrediction

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath("assets/models/model_061-0.7933.h5")
prediction.setJsonPath("assets/json/model_class.json")
prediction.loadModel(num_objects=10)

predictions, probabilities = prediction.predictImage("Jurado.jpg", result_count=3)

for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)

