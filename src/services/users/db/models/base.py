import uuid

from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Index, Text, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from services.users.dto.consts.provided_services_consts import ServicePropositionStatus, ServiceType, ServiceContentType
from services.users.dto.consts.user_consts import UserAccountType

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    uid = Column(String, default=uuid.uuid4)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    service_provider = Column(Boolean, default=0)
    proposed_service = relationship('ProposedService')

    Index('users_uid_idx', uid)


class UserAccount(Base):
    __tablename__ = 'user_accounts'
    id = Column(Integer, primary_key=True)
    uid = Column(String, default=uuid.uuid4)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    user_account_type = Column(Enum(UserAccountType), nullable=False)


class UserExpertise(Base):
    __tablename__ = 'user_expertises'
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'),
                     nullable=False,
                     index=True)
    uid = Column(String)
    expertise_name = Column(String)
    user = relationship(User)
    expertise_level = Column(Integer)
    deleted = Column(Boolean, default=False)


class UserInterest(Base):
    __tablename__ = 'user_interest'
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'),
                     nullable=False,
                     index=True)
    uid = Column(String)
    interest_name = Column(String)
    interest_level = Column(Integer)
    user = relationship(User)
    deleted = Column(Boolean, default=False)


class UserHobby(Base):
    __tablename__ = 'user_hobbies'
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'),
                     nullable=False,
                     index=True)
    uid = Column(String)
    hobby_name = Column(String)
    engagement_level = Column(Integer)
    user = relationship(User)
    deleted = Column(Boolean, default=False)


class UserFeedback(Base):
    __tablename__ = "user_feedbacks"
    id = Column(Integer, primary_key=True)
    feedback_from_user_id = Column(ForeignKey('users.id'),
                                   nullable=False,
                                   index=True)
    feedback_from_user = relationship(User, foreign_keys='UserFeedback.feedback_from_user_id')
    feedback_about_user_id = Column(ForeignKey('users.id'),
                                    nullable=False,
                                    index=True)
    feedback_about_user = relationship(User, foreign_keys='UserFeedback.feedback_about_user_id')
    description = Column(Text, nullable=True)

    feedback_ratings = relationship('FeedbackRating')

    deleted = Column(Boolean, default=False)


class FeedbackRating(Base):
    __tablename__ = "feedback_ratings"
    id = Column(Integer, primary_key=True)
    feedback_rating_type = Column(String)
    feedback_rating_score = Column(Integer)

    user_feedback_id = Column(ForeignKey('user_feedbacks.id'),
                              nullable=False,
                              index=True)
    user_feedback = relationship('UserFeedback', back_populates='feedback_ratings')


class ProposedService(Base):
    __tablename__ = 'proposed_services'
    id = Column(Integer, primary_key=True)
    proposition_owner_id = Column(ForeignKey('users.id'), nullable=False, index=True)
    proposition_owner = relationship('User', back_populates='proposed_service')

    proposition_status = Column(Enum(ServicePropositionStatus))
    service_type = Column(Enum(ServiceType))
    proposition_description = Column(Text)
    service_content_types = relationship('ProposedServiceContentType')


class ProposedServiceContentType(Base):
    __tablename__ = 'proposed_service_content_types'
    id = Column(Integer, primary_key=True)
    service_content_type = Column(Enum(ServiceContentType))

    proposed_service_id = Column(ForeignKey('proposed_services.id'), nullable=False)
    proposed_service = relationship('ProposedService', back_populates='service_content_types')
