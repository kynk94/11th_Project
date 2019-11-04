# LIVE IMAGE GAN  
사진 한장을 넣어서도 움직이는 결과물이 나오도록 만들자.  
Few-shot talking heads와 흡사한 개념, 프로젝트 진행 초기 소스 코드가 없었음.  
## Everybody Dance Now(pix2pix)  
<img src="https://user-images.githubusercontent.com/41245985/68099809-eeeeeb80-ff07-11e9-891e-553d238bedc8.png">  

요약 - pix2pix의 방대하게 학습된 모델을 가져와 전이학습의 형태로 Target Video의 모습을 잘 학습하게 되며, Source Video의 자세를 따라하도록 만든다.  

Target Video로부터 뼈대를 추출하여 Ground Truth를 만들고, 생성자가 뼈대를 기준으로 이미지를 만들어내고 판별자가 식별하는 방식으로 계속해서 이를 학습한다.
그 후에 Source Video로부터 자세만 가져와 생성자가 결과물을 만들어낸다.  
그렇기 때문에 Target Video의 모습을 오랫동안 학습하여야 하며, 하나의 모델당 하나의 Target Video만 표현할 수 있는 것이 특징이다.  
#### Paper  
<a href="https://arxiv.org/abs/1808.07371">https://arxiv.org/abs/1808.07371</a>  
#### 동작 방식  
1. Source Video로부터 Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields을 사용하여 뼈대를 얻는다.  
Pose Estimation git : <a href="https://github.com/ZheC/Realtime_Multi-Person_Pose_Estimation">https://github.com/ZheC/Realtime_Multi-Person_Pose_Estimation</a>  
2. 얻어낸 뼈대를 Target 크기에 맞춘 후, Target 의 뼈대를 겹치는 것으로 똑같이 움직이도록 만든다.  
3. 이 경우 얼굴이 잘 생성되지 못하는데, 이를 Face Gan을 사용하여 얼굴을 만들어낸다.  
아래 GIF의 경우 유리창에 반사되는 모습까지 생성된것이 인상적이다.  
<img src="https://user-images.githubusercontent.com/41245985/68099825-0332e880-ff08-11e9-834e-5a966f3e1c5e.gif">  

## Few Shot(Talking head)
<img src="https://user-images.githubusercontent.com/41245985/68099948-b13e9280-ff08-11e9-930d-9cfe3b33d9e7.png">  
