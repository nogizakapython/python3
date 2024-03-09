import flora1
import flora2

try:
  exec(flora1.main())
  exec(flora2)
except TypeError:
  msg = "問題ありません"
