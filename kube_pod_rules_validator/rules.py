
class ApplyRules(object):
    """
    ApplyRules class implements various rules such as
    image_prefix
    label
    """

    def __init__(self):
        pass

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

