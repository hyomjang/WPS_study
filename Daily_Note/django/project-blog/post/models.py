from django.db import models


class Post(models.Model):
    # 글 제목
    title = models.CharField(max_length=40)
    # 간단설명
    description = models.CharField(max_length=100)
    # # 커버이미지
    # img_cover = models.ImageField(blank=True)
    # 본문내용`
    content = models.TextField()
    # 조회수
    view_count = models.IntegerField(default=0)
    # 좋아요 수
    like_count = models.IntegerField(default=0)
    # 작성자의 IP주소
    #     ip_address = models.IPAddressField(blank=Tue)
    # 생성일자
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s]%s' % (self.description, self.title)
