# flake8: noqa
# There's no way to ignore "F401 '...' imported but unused" warnings in this
# module, but to preserve other warnings. So, don't check this module at all.

# Copyright 2022 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import TYPE_CHECKING

from transformers.utils import _LazyModule


_import_structure = {
    "configuration_ernie": ["ERNIE_PRETRAINED_CONFIG_ARCHIVE_MAP", "ErnieConfig", "ErnieOnnxConfig"],
}

_import_structure["modeling_ernie"] = [
    "ERNIE_PRETRAINED_MODEL_ARCHIVE_LIST",
    "ErnieForCausalLM",
    "ErnieForMaskedLM",
    "ErnieForMultipleChoice",
    "ErnieForNextSentencePrediction",
    "ErnieForPreTraining",
    "ErnieForQuestionAnswering",
    "ErnieForSequenceClassification",
    "ErnieForTokenClassification",
    "ErnieModel",
    "ErniePreTrainedModel",
]

if TYPE_CHECKING:
    from .configuration_ernie import ERNIE_PRETRAINED_CONFIG_ARCHIVE_MAP, ErnieConfig, ErnieOnnxConfig
    from .pytorch_utils import *
    from .modeling_ernie import (
        ERNIE_PRETRAINED_MODEL_ARCHIVE_LIST,
        ErnieForCausalLM,
        ErnieForMaskedLM,
        ErnieForMultipleChoice,
        ErnieForNextSentencePrediction,
        ErnieForPreTraining,
        ErnieForQuestionAnswering,
        ErnieForSequenceClassification,
        ErnieForTokenClassification,
        ErnieModel,
        ErniePreTrainedModel,
    )

else:
    import sys

    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure, module_spec=__spec__)