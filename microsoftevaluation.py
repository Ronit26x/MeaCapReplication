from pycocoevalcap.eval import COCOEvalCap
from pycocotools.coco import COCO
coco = COCO('/content/drive/MyDrive/MeaCap/Flickr30K/Ground_Truth.json')
result = coco.loadRes('/content/drive/MyDrive/MeaCap/outputs/Answer.json')
cocoEval = COCOEvalCap(coco, result)
cocoEval.evaluate()
for metric, score in cocoEval.eval.items():
    print(f'{metric}: {score:.3f}')
