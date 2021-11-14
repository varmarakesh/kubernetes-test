import yaml


class Rules(object):

    def __init__(self, rules_file='rules/rules.yaml'):
        self.rules = self.__load_yaml(rules_file=rules_file)

    def __load_yaml(self, rules_file):
        with open(rules_file, 'r') as rules:
            parsed_yaml = yaml.safe_load(rules)
            return parsed_yaml


class ApplyRules(object):

    def __init__(self):
        self.rules = Rules().rules

    def __validate_label(self, labels):
        return 'team' in labels.keys()

    def __validate_image_prefix(self, images):
        result = True
        for image in images:
            if image.split('/')[0] != 'bitnami':
                return False
        return result

    def validate(self, pods):
        result = []
        for pod in pods:
            image_prefix_rule = self.__validate_image_prefix(
                images=pod.images
            )
            team_label_present = self.__validate_label(labels=pod.labels)
            pod_result = {
                'pod': pod.name,
                'rule_evaluation': [
                    {
                        'name': 'image_prefix',
                        'valid': image_prefix_rule
                    },
                    {
                        'name': 'team_label_present',
                        'valid': team_label_present
                    }
                ]
            }
            result.append(pod_result)
        return result

