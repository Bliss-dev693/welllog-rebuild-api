<<<<<<< HEAD

# welllog-rebuild-api

基于深度学习的测井曲线高精度重构系统。此API使用训练好的模型对缺失的CNL测井曲线进行预测重构。

## 使用方式

启动服务：

```bash
pip install -r requirements.txt
python app.py
```

POST 请求接口：

`POST /predict`

JSON 请求示例：

```json
{
  "AC": [...],
  "GR": [...],
  "RT": [...],
  "RXO": [...]
}
```

## 文件说明

- model_Main2.h5: 主模型文件
- scaler_X2.pkl / scaler_y2.pkl: 训练时使用的标准化器
=======
# welllog-rebuild-api
>>>>>>> 8ad0a685f1813ab60cda238690dc3c9146c487ed
