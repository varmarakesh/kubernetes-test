from datetime import datetime, timezone


class ApplyRules(object):
    """
    ApplyRules class implements the following rules
    image_prefix
    label
    recent_start_time
    """
    ALLOWED_LABEL_KEY = 'team'
    ALLOWED_IMAGE_PREFIX = 'bitnami'
    MAX_POD_AGE_IN_DAYS = 7

    def __init__(self):
        pass

    def __validate_label(self, labels):
        """
        Returns True if pod labels has a key by name ALLOWED_LABEL_KEY and there
        exists a value for the key
        :param labels:
        :return:
        """
        if ApplyRules.ALLOWED_LABEL_KEY in labels.keys():
            if labels[ApplyRules.ALLOWED_LABEL_KEY] is not None:
                return True
        return False

    def __validate_image_prefix(self, images):
        """
        Returns True if all the images in the pod used the prefix
        defined in ALLOWED_IMAGE_PREFIX
        :param images:
        :return:
        """
        result = True
        for image in images:
            if image.split('/')[0] != ApplyRules.ALLOWED_IMAGE_PREFIX:
                return False
        return result

    def __validate_recent_start_time(self, start_time):
        """
        Return True if the pod start_time age does not exceed by MAX_POD_AGE_IN_DAYS
        :param start_time:
        :return:
        """
        now = datetime.now(timezone.utc)
        time_difference = now - start_time
        return time_difference.days > ApplyRules.MAX_POD_AGE_IN_DAYS

    def validate(self, pods):
        result = []
        for pod in pods:
            image_prefix_rule = self.__validate_image_prefix(
                images=pod.images
            )
            team_label_present = self.__validate_label(labels=pod.labels)
            recent_start_time = self.__validate_recent_start_time(start_time=pod.recent_start_time)
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
                    },
                    {
                        'name': 'recent_start_time',
                        'valid': recent_start_time
                    }
                ]
            }
            result.append(pod_result)
        return result

