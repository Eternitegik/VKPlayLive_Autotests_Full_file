from typing import List, Optional
from pydantic import BaseModel


class Category(BaseModel):
    coverUrl: str
    type: str
    title: str
    id: str


class Count(BaseModel):
    viewers: int
    likes: int
    views: int


class AccessRestrictions(BaseModel):
    view: dict


class Stream(BaseModel):
    startTime: int
    daNick: str
    endTime: Optional[int]
    previewUrl: str
    isOnline: bool
    isPublic: bool
    id: str
    category: Category
    data: List[str]
    isLiked: bool
    createdAt: int
    wsChatChannelPrivate: str
    wsChatChannel: str
    hasAccess: bool
    count: Count
    wsStreamChannelPrivate: str
    accessRestrictions: AccessRestrictions
    isHidden: bool
    wsStreamViewersChannel: str
    embedUrl: str
    title: str
    wsStreamChannel: str
    isEnded: bool


class Owner(BaseModel):
    name: str
    nickColor: int
    displayName: str
    hasAvatar: bool
    id: int
    isVerifiedStreamer: bool
    vkplayProfileLink: str
    avatarUrl: str
    nick: str


class Blog(BaseModel):
    owner: Owner
    coverUrl: Optional[str]
    blogUrl: str
    hasAdultContent: bool
    title: str


class StreamBlog(BaseModel):
    stream: Stream
    blog: Blog


class Data(BaseModel):
    streamBlogs: List[StreamBlog]


class Response(BaseModel):
    data: Data
