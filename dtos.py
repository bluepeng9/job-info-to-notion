class CompanyGroup:
    def __init__(self, id, name, created_at, updated_at, business_size, business_type, image_file_name,
                 image_content_type, image_file_size, image_updated_at, current_shard, alternate_names):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        self.business_size = business_size
        self.business_type = business_type
        self.image_file_name = image_file_name
        self.image_content_type = image_content_type
        self.image_file_size = image_file_size
        self.image_updated_at = image_updated_at
        self.current_shard = current_shard
        self.alternate_names = alternate_names


class DutyGroup:
    def __init__(self, group_id):
        self.group_id = group_id


class Employment:
    def __init__(self, duty_groups, id, division, duty_category):
        self.duty_groups = [DutyGroup(**group) for group in duty_groups]
        self.id = id
        self.division = division
        self.duty_category = duty_category


class Job:
    def __init__(self, id, name, title, company_group, start_time, end_time, image_file_name, recruit_type,
                 business_size, business_type, employments, in24hours, gg=None, advertise_id=None):
        self.id = id
        self.name = name
        self.title = title
        self.company_group = CompanyGroup(**company_group)
        self.start_time = start_time
        self.end_time = end_time
        self.image_file_name = image_file_name
        self.recruit_type = recruit_type
        self.business_size = business_size
        self.business_type = business_type
        self.employments = [Employment(**employment) for employment in employments]
        self.in24hours = in24hours
        self.gg = gg

    def __str__(self):
        return f'Job({self.id}, {self.name}, {self.title}, {self.company_group}, {self.start_time}, {self.end_time}, {self.image_file_name}, {self.recruit_type}, {self.business_size}, {self.business_type}, {self.employments}, {self.in24hours}, {self.gg})'
