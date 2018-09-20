def valid_month_abr(month_abr):
    full_names = {'jan': 'January', 'feb': 'February', 'mar': 'March', 'apr': 'April',
                  'may': 'May', 'jun': 'June', 'jul': 'July', 'aug': 'August',
                  'sep': 'September', 'oct': 'October', 'nov': 'November', 'dec': 'December'}
    try:
        mfn=full_names[month_abr]
    except:
        print("Invalid month abbreviation entered")
        exit(1)
    return(mfn)

def seasons_month(month_abr):
    aseson_dict = { }
    mseasons_dict = {'jan':'winter','feb':'winter', 'mar':'spring', 'apr':'sprint',
                    'may':'spring','jun':'summer', 'jul':'summer', 'aug':'summer',
                    'sep':'fall',   'oct':'fall',  'nov':'fall',   'dec':'winter'}
    mms=mseasons_dict[month_abr]
    return(mms)

def month_info(month_abr):   
    month_nums = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
                  'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}

    birth_stones = {'jan': 'Garnet', 'feb': 'Amethyst', 'mar': 'Aquamarine', 'apr': 'Diamond',
                    'may': 'Emerald', 'jun': 'Pearl', 'jul': 'Ruby', 'aug': 'Peridot',
                    'sep': 'Sapphire', 'oct': 'Opal', 'nov': 'Topaz', 'dec': 'Turquoise'}
    mn=month_nums[month_abr]
    bs=birth_stones[month_abr]
    return(mn,bs)
    
if __name__ == '__main__':
    month_abr=str(input('Please enter a abbreviated month, ex jan: '))
    fmn=valid_month_abr(month_abr)
    mms=seasons_month(month_abr)
    mn, bs=month_info(month_abr)
    print("The month is ",fmn,",the number of the month is ", mn,",the birth stone is ", bs, ",and the season is ", mms)
    

    
