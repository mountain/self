# -*- coding: utf-8 -*-

from gym.envs.registration import register


register(
    id='selfx-bounday-candy-v0',
    entry_point='gym_selfx.envs:SelfxBoundaryCandyEnv',
)


register(
    id='selfx-billard-v0',
    entry_point='gym_selfx.envs:SelfxBillardEnv',
    reward_threshold=20000000,
)
