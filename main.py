def main():
    
    m = int(input('Enter the number of male students: ')) 
    f = int(input('Enter the number of female students: ')) 

    total = m + f
    m_perc = m / total * 100
    f_perc = f / total * 100

    print(f'The total number of students is: \t \t {total}')
    print(f'The number of males and females is:  \t \t {m}\t{f}')
    print(f'The percentage of males and females is:  \t {m_perc:.2f}% {f_perc:.2f}%')


    return m_perc, f_perc


if __name__ == '__main__':
    main()
