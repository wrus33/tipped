from django import template
register = template.Library()

@register.filter
def avgcalc(myDemographic, myCategory):
    ratings = []

    for x in myDemographic:
        ratings.append(myCategory)

    intTotal = 0
    intCount = 0
    intLenMyList = len(myDemographic)

    while(intCount <  intLenMyList):
        intTotal += ratings[intCount]
        intCount += 1


return Shift.objects.all().aggregate(Avg('attribute')
