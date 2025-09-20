"""
Core calculation engine for RPA project estimation
"""

import pandas as pd
import config

class RPACalculator:
    def __init__(self):
        self.config = config

    def calculate_annual_volume(self, frequency, volume_per_freq):
        """Calculate annual transaction volume"""
        multiplier = self.config.FREQUENCY_MULTIPLIERS.get(frequency, 1)
        return volume_per_freq * multiplier

    def calculate_annual_hours(self, annual_volume, avg_handle_time_min):
        """Calculate annual hours required"""
        return (annual_volume * avg_handle_time_min) / 60

    def calculate_fte_required(self, annual_hours):
        """Calculate FTE required"""
        productive_hours = self.config.FTE_CONSTANTS['productive_hours']
        shrinkage = self.config.FTE_CONSTANTS['shrinkage_factor']
        return (annual_hours * shrinkage) / productive_hours

    def calculate_automation_potential(self, rules_based, digital_data,
                                      data_formatted, process_stable,
                                      annual_volume, data_type):
        """Calculate automation potential (0-100%)"""
        score = 0

        # Scoring based on answers (max 90 points)
        score += 30 if rules_based in ['Agree', 'Strongly Agree'] else 15 if rules_based == 'Neutral' else 0
        score += 25 if digital_data in ['Agree', 'Strongly Agree'] else 12 if digital_data == 'Neutral' else 0
        score += 20 if data_formatted in ['Agree', 'Strongly Agree'] else 10 if data_formatted == 'Neutral' else 0
        score += 15 if process_stable in ['Agree', 'Strongly Agree'] else 7 if process_stable == 'Neutral' else 0

        # Volume bonus (10 points)
        if annual_volume > 10000:
            score += 10
        elif annual_volume > 5000:
            score += 7
        elif annual_volume > 1000:
            score += 5
        else:
            score += 2

        # Apply data type penalty
        if 'Unstructured' in data_type:
            score *= 0.6
        elif 'Semi-structured' in data_type:
            score *= 0.8

        return min(score, 95)  # Cap at 95%

    def calculate_implementation_ease(self, app_count, logic_complexity,
                                     environment, data_type):
        """Calculate implementation ease (0-100%)"""
        score = 100

        # Deduct for complexity
        if app_count >= 6:
            score -= 40
        elif app_count >= 4:
            score -= 30
        elif app_count >= 3:
            score -= 20
        elif app_count >= 2:
            score -= 10

        if 'Complex' in logic_complexity:
            score -= 30
        elif 'Moderate' in logic_complexity:
            score -= 15

        if 'Citrix' in environment:
            score -= 40
        elif 'Mainframe' in environment:
            score -= 35
        elif 'Web' in environment:
            score -= 20
        elif 'Desktop' in environment:
            score -= 10
        elif 'API' in environment:
            score += 10

        if 'Unstructured' in data_type:
            score -= 25
        elif 'Semi-structured' in data_type:
            score -= 10

        return max(0, min(100, score))

    def calculate_complexity_score(self, data_type, app_count,
                                  logic_complexity, environment):
        """Calculate complexity multiplier"""
        data_mult = self.config.COMPLEXITY_FACTORS['data'].get(data_type, 1.0)
        app_mult = self.config.COMPLEXITY_FACTORS['applications'].get(min(app_count, 6), 2.5)
        logic_mult = self.config.COMPLEXITY_FACTORS['logic'].get(logic_complexity, 1.0)
        env_mult = self.config.COMPLEXITY_FACTORS['environment'].get(environment, 1.5)

        return data_mult * app_mult * logic_mult * env_mult

    def calculate_effort_days(self, process_steps, complexity_score):
        """Calculate development effort in days"""
        base_days = process_steps * self.config.TIMELINE_FACTORS['base_days_per_step']
        dev_days = base_days * complexity_score

        # Add testing and contingency
        testing = self.config.TIMELINE_FACTORS['testing_factor']
        contingency = self.config.TIMELINE_FACTORS['contingency_buffer']

        total_days = dev_days * (1 + testing) * (1 + contingency)
        return dev_days, total_days

    def calculate_costs_and_roi(self, total_days, fte_saved, ai_monthly_cost=0):
        """Calculate costs and ROI"""
        daily_rate = self.config.TIMELINE_FACTORS['daily_rate_default']
        hourly_rate = self.config.FTE_CONSTANTS['hourly_rate_default']
        annual_hours = self.config.FTE_CONSTANTS['annual_work_hours']

        # Costs
        implementation_cost = total_days * daily_rate
        annual_ai_cost = ai_monthly_cost * 12
        total_cost = implementation_cost + annual_ai_cost

        # Savings
        annual_savings = fte_saved * hourly_rate * annual_hours
        net_savings = annual_savings - annual_ai_cost

        # ROI
        if total_cost > 0:
            roi_percentage = ((net_savings - implementation_cost) / implementation_cost) * 100
            payback_months = (implementation_cost / net_savings) * 12 if net_savings > 0 else 999
        else:
            roi_percentage = 0
            payback_months = 999

        return {
            'implementation_cost': implementation_cost,
            'annual_ai_cost': annual_ai_cost,
            'total_cost': total_cost,
            'annual_savings': annual_savings,
            'net_savings': net_savings,
            'roi_percentage': roi_percentage,
            'payback_months': min(payback_months, 999)
        }

    def determine_quadrant(self, automation_potential, implementation_ease):
        """Determine which quadrant the project falls into"""
        if automation_potential >= 50 and implementation_ease >= 50:
            return "🚀 Quick Win"
        elif automation_potential >= 50 and implementation_ease < 50:
            return "💎 Strategic"
        elif automation_potential < 50 and implementation_ease >= 50:
            return "🔧 Fill-in"
        else:
            return "⏸️ Nice to Have"

    def calculate_priority_score(self, automation_potential, roi_percentage,
                                implementation_ease, fte_saved):
        """Calculate priority score (0-100)"""
        # Normalize values
        roi_norm = min(roi_percentage / 500, 1) * 100  # Normalize to 100
        fte_norm = min(fte_saved / 10, 1) * 100  # Normalize to 100

        # Weighted score
        score = (
            automation_potential * 0.30 +
            roi_norm * 0.30 +
            implementation_ease * 0.20 +
            fte_norm * 0.20
        )

        return min(score, 100)