from typing import List, Optional
from pydantic import BaseModel


class WebSocket(BaseModel):
    token: str
    channel: str


class Geo(BaseModel):
    country: int


class Telegram(BaseModel):
    hasAccount: bool
    username: Optional[str]


class Discord(BaseModel):
    hasAccount: bool
    username: Optional[str]
    hasServer: bool
    serverName: Optional[str]


class ExternalApps(BaseModel):
    discord: Discord
    telegram: Telegram


class DialogSettings(BaseModel):
    canSendMyAuthors: bool
    canSendDonation: bool
    sendMsgLevelId: int
    canSendSubscribers: bool
    canSendPaidSubscribers: bool
    canSendAll: bool


class Flags(BaseModel):
    isShareDonationHelperSeen: bool
    hasAcceptedCommonSettings: bool
    hasDialogSettingsPromo: bool
    hasTeaserHelper: bool
    hasRecordHelper: bool
    isTipDonationHelperSeen: bool
    hasMessageButtonHelper: bool
    hasRecommendationTechnologiesAlert: bool
    GDPR: bool
    isShowedRecordHelp: bool
    hasGiftHelper: bool
    isAddPhoneHelperSeen: bool
    hasStreamHelper: bool
    hasMessageHeaderHelper: bool
    hasBlogPostSelectorHelper: bool
    hasBlogPostDraftHelper: bool
    canViewAdultContent:  bool


class EmailConfirmed(BaseModel):
    social: bool
    noSocial: bool


class NewStream(BaseModel):
    telegram: bool
    mobile_push: bool
    standalone: bool
    mail: bool


class Notifications(BaseModel):
    newStream: NewStream


class AuthSource(BaseModel):
    id: str
    type: str
    list: List[str]


class Counts(BaseModel):
    unreadMsg: int


class Response(BaseModel):
    isReadyToMakeReview: bool
    privacyVersion: int
    name: str
    isAdmin: bool
    counts: Counts
    authSource: AuthSource
    problemSubscriptions: Optional[List[str]]
    nickColor: int
    shouldPublicStreamRecord: bool
    displayName: str
    isTutorialFinished: bool
    notifications: Notifications
    avatarUrl: str
    locale: str
    emailConfirmed: EmailConfirmed
    id: int
    unreadMsgCount: int
    blogUrl: str
    email: str
    hasBoostyIntegration: bool
    vkplayProfileLink: str
    hasPayout: bool
    flags: Flags
    hasAvatar: bool
    isTotalBaned: bool
    # dialogSettings: DialogSettings  # Эта переменная пропала после обновления
    nick: str
    isReadOnly: bool
    isStreamer: bool
    externalApps: ExternalApps
    isConfirmationsExists: bool
    isVerifiedStreamer: bool
    timezone: int
    isTestUser: bool
    isBlogger: bool
    selfPublicStreamHidden: bool
    referalConvVersion: int
    geo: Geo
    canBeRaided: bool
    isScheduledForDeletion: bool
    hasPaymentBind: bool
    paidFunctionsAvailable: bool
    shouldStreamRecord: bool
    webSocket: WebSocket
    defaultCurrency: str
    isModerator: bool
