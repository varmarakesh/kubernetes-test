import yaml


class Rules(object):

    def __init__(self, rules_file='rules/rules.yaml'):
        self.rules = self.__load_yaml(rules_file=rules_file)

    def __load_yaml(self, rules_file):
        with open(rules_file, 'r') as rules:
            parsed_yaml = yaml.safe_load(rules)
            return parsed_yaml

    def get_rules(self):
        """
        return rules as dictionary.
        :return:
        """
        return self.rules

    def __validate_image_prefix(self, images):
        result = True
        for image in images:
            if image.split('/')[0] != 'bitnami':
                return False
        return result

    def validate(self, images):
        result = True
        for rule in self.rules:
            if rule['name'] == 'image_prefix':
                image_prefix_rule = self.__validate_image_prefix(
                    images=images
                )
                result = result and image_prefix_rule
        return result

