# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

from manager import db


class IpPool(db.Model):
    __tablename__ = 'Ip_pool'

    host = db.Column(db.String(64), primary_key=True)
    port = db.Column(db.String(64))
    sys_time = db.Column(db.Integer)



class BilibiliLiveRoomInfo(db.Model):
    __tablename__ = 'bilibili_live_room_info'

    sys_id = db.Column(db.Integer, primary_key=True)
    roomId = db.Column(db.Integer)
    uid = db.Column(db.Integer)
    roomName = db.Column(db.String(255))
    showStatus = db.Column(db.Integer)
    showTime = db.Column(db.Integer)
    nickName = db.Column(db.String(255))
    gameName = db.Column(db.String(255))
    hotIndex = db.Column(db.Integer)
    fans = db.Column(db.Integer)
    sys_time = db.Column(db.DateTime)
    sys_timeindex = db.Column(db.Integer)



class ContentList(db.Model):
    __tablename__ = 'content_list'

    sys_id = db.Column(db.Integer, primary_key=True)
    contentType = db.Column(db.ForeignKey('content_type.sys_id'), index=True)
    args1 = db.Column(db.String(64))
    args2 = db.Column(db.String(64))
    taskLevel = db.Column(db.ForeignKey('task_level.sys_id'), index=True)

    content_type = db.relationship('ContentType', primaryjoin='ContentList.contentType == ContentType.sys_id', backref='content_lists')
    task_level = db.relationship('TaskLevel', primaryjoin='ContentList.taskLevel == TaskLevel.sys_id', backref='content_lists')



class ContentType(db.Model):
    __tablename__ = 'content_type'

    sys_id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.ForeignKey('platform.sys_id'), index=True)
    contentType = db.Column(db.String(64))
    qutas = db.Column(db.Integer)

    platform1 = db.relationship('Platform', primaryjoin='ContentType.platform == Platform.sys_id', backref='content_types')



class DouyuRoomInfo(db.Model):
    __tablename__ = 'douyu_room_info'

    sys_id = db.Column(db.Integer, primary_key=True)
    roomId = db.Column(db.Integer, index=True)
    roomName = db.Column(db.String(255))
    showStatus = db.Column(db.Integer)
    showTime = db.Column(db.Integer)
    nickName = db.Column(db.String(255), index=True)
    gameName = db.Column(db.String(64))
    fans = db.Column(db.Integer)
    hotIndex = db.Column(db.Integer)
    sys_time = db.Column(db.DateTime, index=True)
    sys_timeindex = db.Column(db.Integer)



class EgameRoomInfo(db.Model):
    __tablename__ = 'egame_room_info'

    sys_id = db.Column(db.Integer, primary_key=True)
    roomId = db.Column(db.Integer)
    roomName = db.Column(db.String(255))
    nickName = db.Column(db.String(255))
    showStatus = db.Column(db.Integer)
    showTime = db.Column(db.Integer)
    gameName = db.Column(db.String(64))
    fans = db.Column(db.Integer)
    hotIndex = db.Column(db.Integer)
    sys_time = db.Column(db.DateTime)
    sys_timeindex = db.Column(db.Integer)



class HuyaRoomInfo(db.Model):
    __tablename__ = 'huya_room_info'

    sys_id = db.Column(db.Integer, primary_key=True)
    roomId = db.Column(db.Integer)
    roomName = db.Column(db.String(255))
    nickName = db.Column(db.String(255))
    gameName = db.Column(db.String(255))
    fans = db.Column(db.Integer)
    hotIndex = db.Column(db.Integer)
    sys_time = db.Column(db.DateTime)
    sys_timeindex = db.Column(db.Integer)



class Platform(db.Model):
    __tablename__ = 'platform'

    sys_id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(64))
    platformType = db.Column(db.ForeignKey('platform_type.sys_id'), index=True)

    platform_type = db.relationship('PlatformType', primaryjoin='Platform.platformType == PlatformType.sys_id', backref='platforms')



class PlatformType(db.Model):
    __tablename__ = 'platform_type'

    sys_id = db.Column(db.Integer, primary_key=True)
    platformType = db.Column(db.String(64))



class TaskLevel(db.Model):
    __tablename__ = 'task_level'

    sys_id = db.Column(db.Integer, primary_key=True)
    taskLevel = db.Column(db.Integer)



class User(db.Model):
    __tablename__ = 'user'

    sys_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password = db.Column(db.String(64))
    level = db.Column(db.ForeignKey('user_qutas.sys_id'), index=True)

    user_quta = db.relationship('UserQuta', primaryjoin='User.level == UserQuta.sys_id', backref='users')



class UserQuta(db.Model):
    __tablename__ = 'user_qutas'

    sys_id = db.Column(db.Integer, primary_key=True)
    userQutas = db.Column(db.Integer)



class WeiboStatu(db.Model):
    __tablename__ = 'weibo_status'

    sys_id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(64))
    createTime = db.Column(db.String(64))
    statusId = db.Column(db.String(64))
    statusBid = db.Column(db.String(64))
    text = db.Column(db.Text)
    source = db.Column(db.String(64))
    repost = db.Column(db.Integer)
    attitude = db.Column(db.Integer)
    comment = db.Column(db.Integer)
    userId = db.Column(db.BigInteger)
    sys_time = db.Column(db.DateTime)
    sys_timeindex = db.Column(db.Integer)



class WeiboUserinfo(db.Model):
    __tablename__ = 'weibo_userinfo'

    sys_id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.BigInteger)
    userName = db.Column(db.String(64))
    status = db.Column(db.Integer)
    imgUrl = db.Column(db.String(256))
    verified = db.Column(db.String(64))
    verifiedType = db.Column(db.String(64))
    verifiedReason = db.Column(db.String(64))
    closeBlueV = db.Column(db.String(64))
    description = db.Column(db.String(256))
    gender = db.Column(db.String(64))
    mbtype = db.Column(db.Integer)
    urank = db.Column(db.Integer)
    mbrank = db.Column(db.Integer)
    follower = db.Column(db.Integer)
    follow = db.Column(db.Integer)
    sys_time = db.Column(db.DateTime)
    sys_timeindex = db.Column(db.Integer)



class WetvLiveRoomInfo(db.Model):
    __tablename__ = 'wetv_live_room_info'

    sys_id = db.Column(db.Integer, primary_key=True)
    roomId = db.Column(db.Integer)
    uid = db.Column(db.String(128))
    nickName = db.Column(db.String(255))
    showTime = db.Column(db.String(128))
    gameName = db.Column(db.String(128))
    hotIndex = db.Column(db.Integer)
    sys_time = db.Column(db.DateTime)
    sys_timeindex = db.Column(db.Integer)
