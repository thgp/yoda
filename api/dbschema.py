from datetime import datetime
from flask.ext.mongokit import MongoKit, Document

class RootDocumentModel(Document):
    # Foundation class for all of the MongoDB Document Object Models
    __database__ = "yoda"

    structure = {
        'last_modified': datetime,
        'enabled': bool
    }

    default_values = {
        'last_modified': datetime.utcnow(),
        'enabled': True
    }

    use_dot_notation = True
    use_autorefs = True
    skip_validation = False
    use_schemaless = True

    def __repr__(self):
        # A string representation for any object.
        #
        # Returns: String
        return "<%s: %s>" % (self.__class__.__name__, str(self._id))

    @property
    def created_date(self):
        # Pull the created date out of the MongoDB object_id and return that.
        # This value cannot be changed; it is read only.
        #
        # Returns: datetime.datetime
        return self._id.generation_time

    @property
    def last_modified(self):
        # Return the datetime this object was last modified.
        #
        # Returns: datetime.datetime
        return self['last_modified']

    @last_modified.setter
    def last_modified(self, value):
        # Set the datetime this object was last modified.
        #
        # Returns: nothing
        self['last_modified'] = value

    @property
    def is_enabled(self):
        # Is this particular document enabled or not. Instead of deleting
        # documents from MongoDB, we should disable them. This is a
        # read only property
        #
        # Returns: bool
        return self['enabled']

    def save(self):
        # Override the base save() function to automatically set the
        # last_modified time to the current datetime.
        #
        # Returns: whatever the save() function returns
        self['last_modified'] = datetime.utcnow()
        return super(RootDocumentModel, self).save()

    def disable(self, update_database=True):
        # Disable a Document. This function will trigger an automatic database
        # update unless otherwise specified.
        #
        # Parameters:
        #    update_database: bool used to determine if this change should
        #                     immediately be saved to the database or not.
        #
        # Returns: nothing
        self['enabled'] = False

        if update_database:
            self.save()

    def enable(self, update_database=True):
        # Enable a Document. This function will trigger an automatic database
        # update unless otherwise specified.
        #
        # Parameters:
        #    update_database: bool used to determine if this change should
        #                     immediately be saved to the database or not.
        #
        # Returns: nothing
        self['enabled'] = True

        if update_database:
            self.save()


class CodeDocumentModel(RootDocumentModel):
    # A mongo document model to store individual
    __collection__ = 'code'

    structure = {
        'code': unicode,
        'is_valid_syntax': bool
    }

    required_fields = ['code']

    @property
    def has_syntax_been_checked():
        # Determines if the syntax has been checked for this instance of
        # code. If the is_valid_syntax boolean is equal to None, then it's
        # never been syntax checked.
        return is_valid_syntax != None


class CodeSetDocumentModel(RootDocumentModel):
    # A mongo document model to store all references to all versions of a
    # piece of code.
    __collection__ = 'code'

    structure = {
        'versions': [CodeDocumentModel]
    }


class TestCaseDocumentModel(RootDocumentModel):
    __collection__ = 'testcases'
    structure = {
        'code': unicode,
        'description': unicode,
        'function_reference': unicode,
        'function_student': unicode,
        'num_inputs': int,
    }
    required_fields = ['code', 'function_reference', 'function_student', 'num_inputs']
