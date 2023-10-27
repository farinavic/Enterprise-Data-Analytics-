import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Book2.csv')
df['Fecha_Venta'] = pd.to_datetime(df['Fecha_Venta'])
df['DiaSemana'] = df['Fecha_Venta'].dt.dayofweek
df['DiaSemana'] = df['DiaSemana'].map({ 0:'Lunes', 1:'Martes', 2: 'Miércoles', 3: 'Jueves', 
4: 'Viernes', 5:'Sábado', 6:'Domingo'})
ingresos_por_dia = df.groupby('DiaSemana')['Venta'].sum()
ingresos_por_mes = df.groupby(df['Fecha_Venta'].dt.strftime('%Y-%m'))['Venta'].sum()
tasa_crecimiento_mensual = ingresos_por_mes.pct_change()



plt.bar(ingresos_por_dia.index, ingresos_por_dia)
plt.xlabel('Día de la semana')
plt.ylabel('Ingresos')
plt.title('Ingresos por día de la semana')


plt.figure(figsize=(10, 6))
ingresos_por_mes.plot(kind='bar', color='skyblue') 
plt.xlabel('Mes')
plt.ylabel('Ingresos')
plt.title('Ingresos por Mes')
plt.xticks(rotation=45) 


plt.figure(figsize=(10, 6))
tasa_crecimiento_mensual.plot(kind='bar', color='lightgreen')
plt.xlabel('Mes')
plt.ylabel('Tasa de Crecimiento Mensual')
plt.title('Tasa de Crecimiento Mensual de Ingresos')
plt.xticks(rotation=45)

plt.show()

