
class Test1:

  array1 = []

  def input_data(self,data1):
    self.array1.append(data1)
    return self.array1


def main():
  data_count = 3
  t1 = Test1()
  for i in range(data_count):
    data1 = int(input())
    array_sample1 = t1.input_data(data1)

  print(array_sample1)

if __name__ == '__main__':
  main()
