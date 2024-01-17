import pandas as pd
data = {
  "国語":[60,80,100],
  "数学":[65,85,100],
  "英語":[66,88,100]
}
idx = ["A太","B介","C子"]
df = pd.DataFrame(data,index=idx)
df
