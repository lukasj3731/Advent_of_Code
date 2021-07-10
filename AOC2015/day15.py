def solve15():
    ingredients = []
    for line in open('inputs/day15.txt').read().split('\n'):
        components = line.split(': ')
        name = components[0]
        attributes = []
        for attr in components[1].split(', '):
            subcomponents = attr.split(' ')
            attributes.append(int(subcomponents[1]))
        ingredients.append((name, attributes))
    teaspoons = 100
    max_score = 0
    max_score_500_cal = 0
    for a in range(teaspoons + 1):
        for b in range(teaspoons - a + 1):
            for c in range(teaspoons - a - b + 1):
                d = teaspoons - a - b - c
                score = 1
                calories = a * ingredients[0][1][4] + b * ingredients[1][1][4] + \
                           c * ingredients[2][1][4] + d * ingredients[3][1][4]
                for i in range(4):
                    attribute_sum = a * ingredients[0][1][i] + b * ingredients[1][1][i] + \
                                    c * ingredients[2][1][i] + d * ingredients[3][1][i]
                    attribute_sum = max(0, attribute_sum)
                    score *= attribute_sum
                max_score = max(score, max_score)
                if calories == 500:
                    max_score_500_cal = max(score, max_score_500_cal)
    return max_score, max_score_500_cal
