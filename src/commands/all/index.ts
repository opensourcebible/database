import { Command, Flags } from '@oclif/core';

export default class Index extends Command {
  static description = 'Generate All files Database';

  async run() {
    this.log(Index.description);
  }
}
