from Empoyee_Package import FulltimeEmployee
from Empoyee_Package import HourlyEmployee
from Empoyee_Package import Payroll

payroll = Payroll.Payroll()

payroll.add(FulltimeEmployee.FulltimeEmployee('Aman', 'Kumar', 6000))
payroll.add(FulltimeEmployee.FulltimeEmployee('Naman', 'Numar', 6500))
payroll.add(HourlyEmployee.HourlyEmployee('Raman', 'Bumar', 200, 50))
payroll.add(HourlyEmployee.HourlyEmployee('Jaman', 'Sumar', 150, 100))
payroll.add(HourlyEmployee.HourlyEmployee('Baman', 'Dumar', 100, 150))

payroll.print()