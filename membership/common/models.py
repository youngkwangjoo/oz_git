from django.db import models


class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add =True)
    #현재 데이터 생성시간을 ㅣㄱ준으로 생성 - 이후 데이터가 업데이트되도 수정되징낳음 auto_now_add
    updated_at = models.DateTimeField(auto_now =True)
    # 생성되는 시간을 기준으로 일단 생성된다. 이후 데이터가 업데이트되면 시간도 업데이트된다. auto_now

    class Meta:
        abstract = True 
        #데이터 베이스에 위에 칼럼이 추가되지않음

        