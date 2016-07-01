#!/user/bin/env python
# -*- coding: utf-8 -*-
import struct
from AccelBrainBeat.brain_beat import BrainBeat


class BinauralBeat(BrainBeat):
    '''
    具象クラス
    バイノーラルビートとモノラルビートの具象的差異を下位クラスで記述する
    Template Method Patternの構成

    '''

    def write_stream(self, stream, left_chunk, right_chunk, volume):
        '''
        具象メソッド
        バイノーラルビートを生成する

        Args:
            stream:         PyAudioのストリーム
            left_chunk:     左音源に対応するチャンク
            right_chunk:    右音源に対応するチャンク
            volume:         音量

        Returns:
            void
        '''
        if len(left_chunk) != len(right_chunk):
            raise ValueError()

        for i in range(len(left_chunk)):
            data = struct.pack(
                "2f",
                left_chunk[i] * volume,
                right_chunk[i] * volume
            )
            stream.write(data)