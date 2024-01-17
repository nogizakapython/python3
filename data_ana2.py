import pandas as pd
data = [
        [60,65,66],
        [80.85,88],
        [100,100,100]

]
df = pd.DataFrame(data)
df.columns=["国語","数学","英語"]
df.index=["A太","B介","C子"]
df
