
# Iterate list of scores and find the second highest score

def runner_up(scores: list) -> int:
    result = None
    if scores:
        runner_up_score = None
        highest_score = None
        for score in scores:
            if highest_score is None:
                highest_score = score
                continue
            elif not runner_up_score and score <= highest_score:
                runner_up_score = score
            elif not runner_up_score and score >= highest_score:
                runner_up_score = highest_score
                highest_score = score
            elif not runner_up_score:
                runner_up_score = score
            elif score > runner_up_score and score < highest_score:
                runner_up_score = score
            elif score > highest_score:
                runner_up_score = highest_score
                highest_score = score
            elif score < runner_up_score and runner_up_score == highest_score:
                runner_up_score = score
        if runner_up_score is None:
            runner_up_score = highest_score
        if not result:
            result = runner_up_score
    return result


if __name__ == "__main__":
    runner_up([-10, 0, 10])