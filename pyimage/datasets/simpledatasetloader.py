import cv2,os
import numpy as np



class SimpleDatasetLoader:
    
    
    def __init__(self,preprocessors=None):
        
        self.preprocessors = preprocessors
        
        
        if self.preprocessors is None:
            self.preprocessors = []
    
    
    def load(self,imagePaths,verbose=-1):
        
        
        data = []
        labels = []
        
        
        for i,imagePath in enumerate(imagePaths):
            image = cv2.imread(imagePath)
            label = imagePath.split(os.path.sep)[-2]
            
            if self.preprocessors is not None:
                for preprocessor in self.preprocessors:
                    image = preprocessor.preprocess(image)
        
        
            data.append(image)
            labels.append(label)


            if verbose > 0 and i > 0 and (i + 1) % verbose == 0:
                print(f"[INFO] processed {i + 1}/{len(imagePaths)}")
                      
            
                      
        return np.array(data),np.array(labels)
                      
        
            
        
        
        