import logging
import pkg_resources
import atta.io.yaml as attayaml

logger = logging.getLogger('atta')

resource_package = __name__
resource_path_packages = '/'.join(('../data', 'packages.yaml'))
resource_path_sponsors = '/'.join(('../data', 'sponsors.yaml'))

template_packages = pkg_resources.resource_stream(resource_package,
                                                  resource_path_packages)

template_sponsors = pkg_resources.resource_stream(resource_package,
                                                  resource_path_sponsors)

yaml_packages = attayaml.read_yaml(template_packages.name)
yaml_sponsors = attayaml.read_yaml(template_sponsors.name)


class Sponsor:

    def __init__(self, sponsor_name):
        self.name = sponsor_name
        self.package_name = yaml_sponsors[sponsor_name]['package']

        self.content = yaml_sponsors[self.name]
        self.package_content_flag = yaml_packages[self.package_name]
        self.package_content_generic_flag = yaml_packages['generic']

    @property
    def flag_description(self):
        return self.package_content_flag['description']

    @property
    def description(self):
        if self.flag_description:
            return self.content['description']
        else:
            self.flag_description

    @property
    def if_one_true_promotion(self):
        tree = self.package_content_flag['promotion']
        return self._if_one_true_in_2_fold(tree)

    @property
    def if_one_true_web(self):
        tree = self.package_content_flag['promotion']['web']
        return self._if_one_true_in_1_fold(tree)

    @property
    def flag_web_click(self):
        return self.package_content_flag['promotion']['web']['click']

    @property
    def web_click(self):
        if self.flag_web_click:
            return self.content['promotion']['web']['click']
        else:
            return self.flag_web_click

    @property
    def flag_web_click_rank(self):
        return self.package_content_flag['promotion']['web']['click_rank']

    @property
    def web_click_rank(self):
        if self.flag_web_click_rank:
            clicks = self._get_all_sponsor_click()
            click_target = self.content['promotion']['web']['click']
            percentage = click_target / float(sum(clicks))
            return "{:.1%}".format(percentage)
        else:
            return self.flag_web_click_rank

    @property
    def if_one_true_facebook(self):
        tree = self.package_content_flag['promotion']['facebook']
        return self._if_one_true_in_1_fold(tree)

    @property
    def flag_facebook_url(self):
        return self.package_content_flag['promotion']['facebook']['url']

    @property
    def facebook_url(self):
        if self.flag_facebook_url:
            return self.content['promotion']['facebook']['url']
        else:
            return self.flag_facebook_url

    @property
    def flag_facebook_reach(self):
        return self.package_content_flag['promotion']['facebook']['reach']

    @property
    def facebook_reach(self):
        if self.flag_facebook_reach:
            return self.content['promotion']['facebook']['reach']
        else:
            return self.flag_facebook_reach

    @property
    def flag_facebook_reach_rank(self):
        return self.package_content_flag['promotion']['facebook']['reach_rank']

    @property
    def facebook_reach_rank(self):
        if self.flag_facebook_reach_rank:
            data = self._get_all_sponsor_fb_field('reach')
            data_target = self.content['promotion']['facebook']['reach']
            percentage = data_target / float(sum(data))
            return "{:.1%}".format(percentage)
        else:
            return self.flag_facebook_reach_rank

    @property
    def flag_facebook_engagement(self):
        return self.package_content_flag['promotion']['facebook']['engagement']

    @property
    def facebook_engagement(self):
        if self.flag_facebook_engagement:
            return self.content['promotion']['facebook']['engagement']
        else:
            return self.flag_facebook_engagement

    @property
    def flag_facebook_engagement_rank(self):
        return self.package_content_flag['promotion']['facebook'][
            'engagement_rank']

    @property
    def facebook_engagement_rank(self):
        if self.flag_facebook_reach_rank:
            data = self._get_all_sponsor_fb_field('engagement')
            data_target = self.content['promotion']['facebook']['engagement']
            percentage = data_target / float(sum(data))
            return "{:.1%}".format(percentage)
        else:
            return self.flag_facebook_engagement_rank

    @property
    def if_one_true_booth(self):
        tree = self.package_content_flag['booth']
        return self._if_one_true_in_1_fold(tree)

    @property
    def flag_booth_participant(self):
        return self.package_content_flag['booth']['participant']

    @property
    def boot_participant(self):
        if self.flag_booth_participant:
            return self.content['booth']['participant']
        else:
            return self.flag_booth_participant

    # @property
    # def flag_booth_participant_rank(self):
    #     return self.package_content_flag['booth']['participant_rank']
    #
    # @property
    # def boot_participant_rank(self):
    #     if self.flag_booth_participant_rank:
    #         data = self._get_all_sponsor_booth_participant()
    #         data_target = self.content['booth']['participant']
    #         percentage = data_target / float(sum(data))
    #         return "{:.1%}".format(percentage)
    #     else:
    #         return self.flag_booth_participant

    @property
    def if_one_true_workshop(self):
        tree = self.package_content_flag['workshop']
        return self._if_one_true_in_1_fold(tree)

    @property
    def flag_workshop_pictures(self):
        return self.package_content_flag['workshop']['pictures']

    @property
    def workshop_pictures(self):
        if self.flag_workshop_pictures:
            return self.content['workshop']['pictures']
        else:
            return self.flag_workshop_pictures

    @property
    def flag_workshop_description(self):
        return self.package_content_flag['workshop']['description']

    @property
    def workshop_description(self):
        if self.flag_workshop_description:
            return self.content['workshop']['description']
        else:
            return self.flag_workshop_description

    @property
    def flag_workshop_event_url(self):
        return self.package_content_flag['workshop']['event_url']

    @property
    def workshop_event_url(self):
        if self.flag_workshop_event_url:
            return self.content['workshop']['event_url']
        else:
            return self.flag_workshop_event_url

    def _if_one_true_in_1_fold(self, tree):
        flag = False
        for key in tree.keys():
            if tree[key]:
                flag = True

        return flag

    def _if_one_true_in_2_fold(self, tree):
        flag = False
        for entry in tree.keys():
            for key in tree[entry].keys():
                if tree[entry][key]:
                    flag = True

        return flag

    def _get_all_sponsor_click(self):
        clicks = []
        for sponsor in yaml_sponsors.keys():
            clicks.append(yaml_sponsors[sponsor]['promotion']['web']['click'])

        return clicks

    def _get_all_sponsor_fb_field(self, field):
        all_data = []
        for sponsor in yaml_sponsors.keys():
            data = yaml_sponsors[sponsor]['promotion']['facebook'][field]
            all_data.append(data)

        return all_data

    def _get_all_sponsor_booth_participant(self):
        all_data = []
        for sponsor in yaml_sponsors.keys():
            data = yaml_sponsors[sponsor]['boot']['participant']
            all_data.append(data)

        return all_data


def get_all_sponsors():
    sponsors = []
    for entry in yaml_sponsors:
        sponsor = Sponsor(entry)
        # TODO: to port these debug information to be a part of test scripts
        # description = sponsor.description
        #
        # flag_promotion = sponsor.if_one_true_promotion
        #
        # flag_web = sponsor.if_one_true_web
        # web_click = sponsor.web_click
        # web_click_rank = sponsor.web_click_rank
        #
        # flag_facebook = sponsor.if_one_true_facebook
        # flag_facebook_reach = sponsor.flag_facebook_reach
        # facebook_reach = sponsor.facebook_reach
        # flag_facebook_reach_rank = sponsor.flag_facebook_reach_rank
        # facebook_reach_rank = sponsor.facebook_reach_rank
        #
        # flag_facebook_engagement = sponsor.flag_facebook_engagement
        # facebook_engagement = sponsor.facebook_engagement
        # flag_facebook_engagement_rank = sponsor.flag_facebook_engagement_rank
        # facebook_engagement_rank = sponsor.facebook_engagement_rank
        #
        # flag_booth = sponsor.if_one_true_booth
        # flag_booth_participant = sponsor.flag_booth_participant
        # booth_participant = sponsor.boot_participant
        # # flag_booth_participant_rank = sponsor.flag_booth_participant_rank
        # # booth_participant_rank = sponsor.booth_participant_rank
        #
        # flag_workshop = sponsor.if_one_true_workshop
        # workshop_pictures = sponsor.flag_workshop_pictures
        # workshop_description = sponsor.workshop_description
        # workshop_event_url = sponsor.workshop_event_url
        # pass

        sponsors.append(sponsor)

    return sponsors
