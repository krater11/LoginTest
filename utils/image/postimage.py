import os
import uuid
from django.db import models


def evaluation_directory_path(product_id, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("evaluations", filename)


class ProductEvaluationImage(models.Model):
    evaluation = models.ForeignKey(
        ProductEvaluation, related_name="evaluation_images", on_delete=models.CASCADE, verbose_name="关联评论")
    images = models.FileField(
        null=True, blank=True, upload_to=evaluation_directory_path, verbose_name="商品评价图片")
    class Meta:
        verbose_name = "商品评价关联图"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.evaluation.detail_content
