print(f'''30 Day Journal
''')

for i in range(1,31):
  user = input(f'Day {i:^2}:: ')
  print()
  journal=f'Journal Day {i:^2}'
  print(f'{journal:^30}')
  print(f'''{user:^30}
  
  ''')
  
