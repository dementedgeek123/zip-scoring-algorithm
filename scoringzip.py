#!/usr/bin/python3

import requests
import json
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
import statistics

@dataclass
class ScoringWeights:
    """Configurable weights for scoring model"""
    # Historical Performance (45%)
    price_appreciation: float = 0.25
    income_levels: float = 0.15
    days_on_market: float = 0.05

    # Future Potential (55%)
    population_growth: float = 0.15
    employment_growth: float = 0.15
    business_activity: float = 0.10
    infrastructure: float = 0.10
    building_permits: float = 0.05


class CensusDataFetcher:
    BASE_URL = "https://api.census.gov/data"

    def __init__(self):
        self.session = requests.Session()

    def get_zip_to_county(self, zipcode: str) -> Optional[Dict]:
        try:
            url = f"{self.BASE_URL}/2021/acs/acs5"
            params = {
                'get': 'NAME',
                'for': f'zip code tabulation area:{zipcode}'
            }
            response = self.session.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if len(data) > 1:
                    return {'zipcode': zipcode, 'name': data[1][0]}
            return None
        except Exception as e:
            print(f"Error fetching ZIP info: {e}")
            return None

    def get_demographic_data(self, zipcode: str) -> Dict:
        try:
            url = f"{self.BASE_URL}/2021/acs/acs5"

            variables = [
                'B19013_001E', 'B01003_001E', 'B25077_001E', 'B25002_002E',
                'B25002_003E', 'B23025_005E', 'B23025_003E', 'B15003_022E',
                'B15003_023E', 'B15003_024E', 'B15003_025E', 'B15003_001E',
            ]

            params = {
                'get': ','.join(variables),
                'for': f'zip code tabulation area:{zipcode}'
            }

            response = self.session.get(url, params=params, timeout=10)

            if response.status_code == 200:
                data = response.json()
                if len(data) > 1:
                    headers = data[0]
                    values = data[1]

                    result = {}
                    for i, header in enumerate(headers):
                        try:
                            val = int(values[i]) if values[i] and values[i] != '-666666666' else 0
                            result[header] = val
                        except (Value employment_data: Dict) -> Tuple[float, str]:
        growth_1yr = employment_data.get('employment_growth_1yr', 0)
        unemployment = employment_data.get('unemployment_rate', 0.05)

        employment_score = self.normalize_score(growth_1yr * 100, -2, 5)
        unemployment_score = self.normalize_score(unemployment, 0.02, 0.10, higher_is_better=False)

        score = (employment_score * 0.7 + unemployment_score * 0.3)

        if growth_1yr >= 0.03 and unemployment <= 0.04:
            explanation = "Strong job market, excellent economic foundation"
        elif growth_1yr >= 0.015:
            explanation = "Growing job market"
        elif growth_1yr >= 0:
            explanation = "Stable employment"
        else:
            explanation = "Declining jobs, economic concerns"

        return score, explanation

    def score_business_activity(self, business_data: Dict) -> Tuple[float, str]:
        growth_rate = business_data.get('business_growth_rate', 0)
        score = self.normalize_score(growth_rate * 100, -1, 6)

        if growth_rate >= 0.04:
            explanation = "Thriving business ecosystem"
        elif growth_rate >= 0.02:
            explanation = "Healthy business growth"
        else:
            explanation = "Limited business growth"

        return score, explanation

    education_rate = census_data.get('college_education_rate', 0.3)
        unemployment = census_data.get('unemployment_rate', 0.05)

        education_score = self.normalize_score(education_rate, 0.15, 0.55)
        unemployment_score = self.normalize_score(unemployment, 0.02, 0.10, higher_is_better=False)

        score = (education_score * 0.6 + unemployment_score * 0.4)

        if education_rate >= 0.45:
            explanation = "Highly educated population, quality infrastructure"
        elif educ
    def score_building_permits(self, permit_data: Dict) -> Tuple[float, str]:
        change_rate = permit_data.get('permits_change_rate', 0)

        if 0.02 <= change_rate <= 0.05:
            score = 9.0
            explanation = "Optimal permit activity, balanced growth"
        elif 0 <= change_rate < 0.02:
            score = 7.0
            explanation = "Modest permit growth"
        elif 0.05 < change_rate <= 0.10:
            score = 6.0
            explanation = "High permit activity, watch for oversupply"
        elif change_rate > 0.10:
            score = 4.0
            explanation = "Very high construction, oversupply risk"
        else:
            score = 5.0
            explanation = "Declining permits, demand concerns"

        return score, explanation

    def calculate_score(self, zipcode: str) -> Dict:
        print(f"\nAnalyzing ZIP code: {zipcode}")
        print("=" * 60)

        print("Fetching data...")
        census_data = self.census.get_demographic_data(zipcode)
        housing_data = self.housing.get_housing_metrics(zipcode)
        employment_data = self.economic.get_employment_data(zipcode)
        business_data = self.economic.get_business_activity(zipcode)
        permit_data = self.economic.get_building_permits(zipcode)
        population_growth = self.census.get_population_growth(zipcode)

        if not census_data:
            return {'error': 'Could not fetch data for this ZIP code', 'zipcode': zipcode}

        scores = {}
        explanations = {}

        median_income = census_data.get('B19013_001E', 0)
        scores['income'], explanations['income'] = self.score_income_levels(median_income)
        scores['appreciation'], explanations['appreciation'] = self.score_price_appreciation(housing_data)

        days_on_market = housing_data.get('days_on_market', 45)
        scores['days_on_market'], explanations['days_on_market'] = self.score_days_on_market(days_on_market)

        scores['population_growth'], explanations['population_growth'] = self.score_population_growth(population_growth)
        scores['employment'], explanations['employment'] = self.score_employment_growth(employment_data)
        scores['business'], explanations['business'] = self.score_business_activity(business_data)
        scores['infrastructure'], explanations['infrastructure'] = self.score_infrastructure(census_data)
        scores['permits'], explanations['permits'] = self.score_building_permits(permit_data)

        final_score = (
            scores['appreciation'] * self.weights.price_appreciation +
            scores['income'] * self.weights.income_levels +
            scores['days_on_market'] * self.weights.days_on_market +
            scores['population_growth'] * self.weights.population_growth +
            scores['employment'] * self.weights.employment_growth +
            scores['business'] * self.weights.business_activity +
            scores['infrastructure'] * self.weights.infrastructure +
            scores['permits'] * self.weights.building_permits
        )

        if final_score >= 8.0:
            recommendation = "EXCELLENT - Strong flip potential"
            risk_level = "Low"
        elif final_score >= 6.5:

    print(f"\n{'KEY METRICS':^60}")
    print("-" * 60)
    raw = results['raw_data']
    print(f"Median Income: ${raw['median_income']:,}")
    print(f"Median Home Value: ${raw['median_home_value']:,}")
    print(f"Population: {raw['population']:,}")
    print(f"Vacancy Rate: {raw['vacancy_rate']}%")
    print(f"Unemployment Rate: {raw['unemployment_rate']}%")
    print(f"College Education Rate: {raw['college_education_rate']}%")
    print(f"Population Growth Rate: {raw['population_growth_rate']}%")
    print()


def main():
    import sys

    print("=" * 60)
    print("Zip Based Scoring System Analyzer by RT")
    print("=" * 60)

    if len(sys.argv) > 1:
        zipcode = sys.argv[1]
    else:
        zipcode = input("\nEnter ZIP code: ").strip()

    if not zipcode.isdigit() or len(zipcode) != 5:
        print("Error: Please enter a valid 5-digit ZIP code")
        return

    scorer = FlipScorer()
    results = scorer.calculate_score(zipcode)
    print_results(results)
