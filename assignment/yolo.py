from imageai.Detection import ObjectDetection




def yolo(resim):
    detector = ObjectDetection()
    model_path = "yolov3.pt"
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(model_path)
    detector.loadModel()


    detections = detector.detectObjectsFromImage(
        input_image=resim, 
        output_image_path="output_image.jpg", 
        minimum_percentage_probability=30)
    
    return detections


def sayim(x):
    toplam={}

    for i in toplam:
        if i["name"] in toplam:
            toplam[i["name"]]+=1
        else:
            toplam[i["name"]]=1
    return toplam