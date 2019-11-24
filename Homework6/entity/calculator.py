class Calculator:
    @staticmethod
    def total_weight_salt(chef):
        final_weight = 0

        if not chef:
            return final_weight

        total = chef.salt
        for items in total:
            final_weight += items.weight

        return final_weight

    @staticmethod
    def total_calories_salt(chef):
        final_calories = 0

        if not chef:
            return final_calories

        total = chef.salt
        for items in total:
            final_calories += items.calories

        return final_calories
