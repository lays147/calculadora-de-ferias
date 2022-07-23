from entities.constants import ABONO_DAYS, MONTH_DAYS
from entities.inss import inss_discount
from entities.lion import lion_discount

try:
    # Salário Info
    salary = float(input("Digite seu salário: R$"))
    day_of_work = salary / MONTH_DAYS
    one_third_of_salary = salary / 3

    # Vacation Info
    vacation_days = int(input("Digite quantos dias de férias você gostaria de tirar: "))
    if vacation_days > 30:
        print("Quantidade de dias de férias inválida.")
        exit()

    vacation_bonus_day_value = one_third_of_salary / MONTH_DAYS
    vacation_bonus = vacation_bonus_day_value * vacation_days

    # Abono Info
    abono_pecuniario = input("Vai vender 10 dias? 1 para sim, 0 para não ")
    if abono_pecuniario not in ["0", "1"] or vacation_days > 20:
        print("Opção inválida para abono pecuniário.")
        exit()

    abono_amount = one_third_of_salary if abono_pecuniario == "1" else 0
    abono_bonus_amount = abono_amount / 3

    # Vacation Calculation
    # Abono does not suffer Taxing! Yay!
    vacation_salary = (day_of_work * vacation_days) + vacation_bonus

    # Taxes deductions
    inss_deduction = inss_discount(salary=vacation_salary)
    lion_deduction = lion_discount(salary=vacation_salary, inss_discount=inss_deduction)

    # Liquid Vacation Salary
    vacation_liquid_salary = (
        vacation_salary
        - inss_deduction
        - lion_deduction
        + abono_bonus_amount
        + abono_amount
    )

    # Remaining Salary
    remaining_salary = day_of_work * (MONTH_DAYS - vacation_days)
    remaining_salary_inss_deduction = inss_discount(remaining_salary)
    remaining_salary_lion_deduction = lion_discount(
        salary=remaining_salary,
        inss_discount=remaining_salary_inss_deduction,
    )
    remaining_liquid_salary = (
        remaining_salary
        - remaining_salary_inss_deduction
        - remaining_salary_lion_deduction
    )

    # Vacation Info
    remaining_vacation_days = (
        MONTH_DAYS - vacation_days
        if abono_pecuniario == "0"
        else MONTH_DAYS - vacation_days - ABONO_DAYS
    )

    resume = f"""
    Eis aqui seu cálculo de férias - APROVEITE!


    Seu salário: R$ {salary:.2f}
    Dias de férias: {vacation_days}
    Proporcional de férias: R$ {vacation_salary:.2f}
    Descontos do INSS:  R$ {inss_deduction:.2f}
    Descontos do IR:  R$ {lion_deduction:.2f}
    Abono Pecuniário:  R$ {abono_amount:.2f}
    Valor à receber de Férias: R$ {vacation_liquid_salary:.2f}
    Valor à receber de Salário: R$ {remaining_liquid_salary:.2f}
    Dias de férias restantes para agendamento {remaining_vacation_days}
    Total no mês: R$ {vacation_liquid_salary+remaining_liquid_salary:.2f}

    Lembre-se que os valores relativos às férias você recebe até 2 dias antes do início das suas férias.
    Agora os valores relativos ao salário deve seguir de acordo com o calendário de sua empresa.
    """
    print(resume, sep="/n")
except KeyboardInterrupt:
    print("Obrigado por usar esse script!")
