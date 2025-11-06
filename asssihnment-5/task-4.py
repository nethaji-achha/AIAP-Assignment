class ApplicantScorer:
    def __init__(self, weights=None):
        """
        Initializes the scorer with optional custom feature weights.
        :param weights: dict mapping feature names to their weights
        """
        # Default feature weights (role-agnostic, non-demographic)
        self.default_weights = {
            'years_experience': 2.0,        # integer count of years
            'education_level': 1.5,         # 0=none, 1=HS, 2=BSc, 3=MSc, 4=PhD
            'skills_matched': 2.5,          # count of matched required skills
            'certifications': 1.0,          # count of relevant certs
            'leadership_experience': 1.0,   # years or binary (0/1)
            'portfolio_quality': 2.0,       # 0–10
            'interview_score': 3.0,         # 0–10
            'coding_test_score': 3.0,       # 0–10
            'culture_fit': 1.5              # 0–10
        }
        if weights:
            self.weights = {**self.default_weights, **weights}
        else:
            self.weights = self.default_weights

    def score(self, applicant_features):
        """
        Computes a score for a job applicant given their features.
        :param applicant_features: dict containing the applicant's feature values.
        :return: float score
        """
        score = 0.0
        for feature, weight in self.weights.items():
            value = applicant_features.get(feature, 0)
            score += value * weight
        return score

    def score_applicants(self, applicants):
        """
        Scores a list of applicants.
        :param applicants: list of dicts of applicant features
        :return: list of tuples (applicant_dict, score), sorted by score descending
        """
        scored_applicants = []
        for applicant in applicants:
            s = self.score(applicant)
            scored_applicants.append((applicant, s))
        # Sort by score descending
        scored_applicants.sort(key=lambda x: x[1], reverse=True)
        return scored_applicants


if __name__ == '__main__':
    import argparse
    import json
    from typing import List, Dict, Any

    parser = argparse.ArgumentParser(description='Score job applicants from a JSON file and print a ranked list.')
    parser.add_argument('--input', '-i', type=str, help='Path to JSON file containing a list of applicants')
    parser.add_argument('--weights', '-w', type=str, help='Optional JSON string with custom feature weights')
    parser.add_argument('--top', '-k', type=int, default=0, help='Show only top K applicants (0 = show all)')
    args = parser.parse_args()

    custom_weights = None
    if args.weights:
        custom_weights = json.loads(args.weights)

    scorer = ApplicantScorer(weights=custom_weights)

    def load_applicants(path: str) -> List[Dict[str, Any]]:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError('Input JSON must be a list of applicant objects')
        return data

    def prompt_float(msg: str, default: float = 0.0) -> float:
        try:
            raw = input(msg).strip()
            return float(raw) if raw else default
        except Exception:
            return default

    def prompt_int(msg: str, default: int = 0) -> int:
        try:
            raw = input(msg).strip()
            return int(raw) if raw else default
        except Exception:
            return default

    if not args.input:
        print('Interactive mode: enter applicant details. Leave blank to use defaults (0).')
        try:
            num = prompt_int('How many applicants? ', 1)
        except Exception:
            num = 1
        applicants: list[dict] = []
        for i in range(num):
            print(f"\nApplicant {i+1}")
            name = input('Name: ').strip() or f'Applicant #{i+1}'
            applicant = {
                'name': name,
                'years_experience': prompt_int('Years of experience (int): ', 0),
                'education_level': prompt_int('Education level 0-4 (int): ', 0),
                'skills_matched': prompt_int('Matched skills count (int): ', 0),
                'certifications': prompt_int('Relevant certifications count (int): ', 0),
                'leadership_experience': prompt_float('Leadership experience years or 0/1: ', 0.0),
                'portfolio_quality': prompt_float('Portfolio quality 0-10: ', 0.0),
                'interview_score': prompt_float('Interview score 0-10: ', 0.0),
                'coding_test_score': prompt_float('Coding test score 0-10: ', 0.0),
                'culture_fit': prompt_float('Culture fit 0-10: ', 0.0)
            }
            applicants.append(applicant)

        scored = scorer.score_applicants(applicants)
        top_n = args.top if args.top and args.top > 0 else len(scored)
        for rank, (app, s) in enumerate(scored[:top_n], start=1):
            name = app.get('name', f'Applicant #{rank}')
            print(f"{rank}. {name} - score: {s:.2f}")
        raise SystemExit(0)

    applicants = load_applicants(args.input)
    scored = scorer.score_applicants(applicants)

    top_n = args.top if args.top and args.top > 0 else len(scored)
    for rank, (app, s) in enumerate(scored[:top_n], start=1):
        name = app.get('name', f'Applicant #{rank}')
        print(f"{rank}. {name} - score: {s:.2f}")
