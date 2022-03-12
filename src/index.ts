import * as oclif from '@oclif/core';

if (process.env.NODE_ENV !== 'production') {
  oclif.settings.debug = true;
}

oclif.run().then(oclif.flush).catch(oclif.Errors.handle);
