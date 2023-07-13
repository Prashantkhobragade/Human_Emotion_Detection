# **Human Emotion Detection**

This project aims to develop a computer vision (CV) model capable of detecting and classifying human emotions into three categories: angry, happy, and sad. The model utilizes deep learning techniques and is trained on a labeled dataset of facial images representing different emotional states.

## Dataset
The dataset used for training and evaluation consists of a collection of facial images labeled with the corresponding emotions: angry, happy, and sad. Each image is preprocessed to extract the facial features necessary for emotion detection. The dataset is divided into three subsets: training, validation, and testing, to ensure accurate evaluation of the model's performance.


## Evaluation
The trained model is evaluated using the testing subset of the dataset. During evaluation, the model takes facial images as input and predicts the corresponding emotions. The predicted emotions are then compared with the ground truth labels to assess the model's accuracy on CetecoricalCrossEntropy

## Deployment
Once the ONNX quantization is applied to the emotion detection model, it can be deployed for real-time emotion detection on new, unseen facial images using FastApi. The quantized model can be integrated into various applications, such as video surveillance systems, virtual assistants, and social robots, to enhance human-computer interaction and understand users' emotional states.

## ONNX Quantization
To reduce the model size and optimize its deployment, the ONNX quantization technique is applied. ONNX (Open Neural Network Exchange) is an open format for representing deep learning models, and quantization is a process that reduces the precision of model weights and activations to minimize memory requirements.

By employing ONNX quantization, the size of the emotion detection model is reduced from 1GB to 83MB while still maintaining satisfactory accuracy and performance. This reduction in model size allows for more efficient storage, faster inference times, and enables deployment on resource-constrained environments.

## **Tech Stack Used**
 1. Python
 2. FastAPI
 3. Wandb
 4. HuggingFace ViT
 5. ONNX Quantization

## How To Run?

## **Future Improvements**
Here are a few potential areas for future improvement and development of the Human Emotion Detection CV Project:
 
1. **Expanded Dataset:** Increase the diversity and size of the dataset to improve the model's generalization and robustness.

2. **Fine-tuning:** Experiment with different hyperparameters, model architectures, or pre-trained models to achieve even better performance.
 
3. **Real-time Optimization:** Optimize the model for real-time performance on edge devices or resource-constrained environments.
 
4. **Additional Emotion Classes:** Extend the model to detect and classify more emotional states beyond angry, happy, and sad.

## Acknowledgments
This project builds upon various open-source libraries, frameworks, and datasets. We would like to acknowledge the contributions of the research community and express our gratitude to the creators and maintainers of these resources.

## License
This project is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt). Feel free to use, modify, and distribute the code and associated materials as per the terms of the license.
