def find_product(num, store_product):
  start = 0
  end = len(store_product) - 1
  while start <= end:
    mid = (start + end) // 2
    if store_product[mid] == num:
      return "yes"
    elif store_product[mid] < num:
      start = mid + 1
    else:
      end = mid - 1
  return "no"


#가게 부품개수와 번호 입력받기
n = int(input())
store_product = list(map(int, input().split()))
store_product.sort()

#고객이 사려하는 부품개수와 번호 입력받기
m = int(input())
customer_product = list(map(int, input().split()))

for i in range(m):
  yes_or_no = find_product(customer_product[i], store_product)
  print(yes_or_no, end=' ')